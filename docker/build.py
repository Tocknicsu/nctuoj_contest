#!/usr/bin/env python3
import sys
import argparse
import os
import json
import subprocess as sp

CONFIG_FILE = "./config.json"

def get_container_info(name):
    p = sp.Popen(["docker", "inspect", name], stdout=sp.PIPE)
    stdout, stderr = p.communicate()
    result = json.loads(stdout.decode())
    return result[0]

def build_api():
    config = json.load(open(CONFIG_FILE, 'r'))
    try:
        os.makedirs(config['api']['DATA_ROOT'])
    except:
        pass
    for x in range(config['api']['number']):
        cmd = [
            "docker", "run", "-itd", "--name", "%s_api_%d"%(config['prefix'], x),
            "--link", "%s_db:%s_db"%(config['prefix'], config['prefix']),
            "-e", "DB_NAME=%s"%(config['DB']['POSTGRES_DB']),
            "-e", "DB_USER=%s"%(config['DB']['POSTGRES_USER']),
            "-e", "DB_PASSWORD=%s"%(config['DB']['POSTGRES_PASSWORD']),
            "-e", "DB_HOST=%s_db"%(config['prefix']),
            "-e", "JUDGE_TOKEN=%s"%(config['judgetoken']),
            "-e", "SB_TOKEN=%s"%(config['sbtoken']),
            "-v", "%s:/mnt/oj/"%(config['api']['DATA_ROOT']),
            "%s_api"%(config['prefix']),
        ]
        print(cmd)
        sp.call(cmd)

def build_web():
    config = json.load(open(CONFIG_FILE, 'r'))
    try:
        os.makedirs(config['web']['DATA_ROOT'])
    except:
        pass
    cmd = [
        "docker", "run", "-itd", "--name", "%s_web"%(config['prefix']),
        "-e", "BASE_URL=%s"%(config["web"]['BASE_URL']),
        "-v", "%s:/mnt/oj_web/"%(config['web']['DATA_ROOT']),
        "%s_web"%(config['prefix']),
    ]
    print(cmd)
    sp.call(cmd)

def build_db():
    config = json.load(open(CONFIG_FILE, 'r'))
    cmd = [
        "docker", "run", "-itd", "--name", "%s_db"%(config['prefix']),
    ]
    for x in config['DB']:
        cmd += ["-e", "%s=%s"%(x, config['DB'][x])]
    cmd += ["%s_db"%(config['prefix'])]
    print(cmd)
    sp.call(cmd)

def build_judge():
    config = json.load(open(CONFIG_FILE, 'r'))
    for x in range(config['judge']['number']):
        cmd = ["docker", "run", "-itd", "--privileged",
                "--name", "%s_judge_%d"%(config['prefix'], x),
                "-e", "BASE_URL=%s"%(config['judge']['BASE_URL']),
                "-e", "JUDGE_TOKEN=%s"%(config['judgetoken']),
                "%s_judge"%(config["prefix"])]
        print(cmd)
        sp.call(cmd)

def build_image(name, directory):
    if sp.call(["docker", "build", "-t", name, directory]):
        print("Docker Build Broken.")
        sys.exit(1)

def build_images():
    print("=====>Building Docker...")
    config = json.load(open(CONFIG_FILE, 'r'))
    build_image("%s_db"%(config["prefix"]), "./db/")
    build_image("%s_api"%(config['prefix']), "./api/")
    build_image("%s_judge"%(config['prefix']), "./judge/")
    build_image("%s_web"%(config['prefix']), "./web/")
    print("=====>Docker Build Done.")

def print_config():
    config = json.load(open(CONFIG_FILE, 'r'))
    print(config)
    db = get_container_info('%s_db'%(config['prefix']))
    print(db['NetworkSettings']['IPAddress'])
    for x in range(config['api']['number']):
        api = get_container_info('%s_api_%s'%(config['prefix'], x,))
        print(api['NetworkSettings']['IPAddress'])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", help="create db", action="store_true")
    parser.add_argument("-api", help="create api", action="store_true")
    parser.add_argument("-web", help="create web", action="store_true")
    parser.add_argument("-judge", help="create judge", action="store_true")
    parser.add_argument("-images", help="build images(db, api, web, judge)", action="store_true")
    parser.add_argument("-all", help="create db api web judge", action="store_true")
    parser.add_argument("-config", help="print config", action="store_true")
    parser.add_argument("-file", help="specify config file", nargs="?", default="./config.json")
    args = parser.parse_args()
    CONFIG_FILE = args.file
    if(os.getuid() != 0):
        print("This program need root! Do you want to run it as root?(Y/n)")
        x = input().lower()
        if x == "y" or x == "":
            os.execv("/usr/bin/sudo", ["sudo", "-E",] + sys.argv)
        else:
            sys.exit(0)
    if args.images:
        build_images()
    if args.config:
        print_config()
    if args.db or args.all:
        build_db()
    if args.api or args.all:
        build_api()
    if args.web or args.all:
        build_web()
    if args.judge or args.all:
        build_judge()


