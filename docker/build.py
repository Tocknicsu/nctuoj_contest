#!/usr/bin/env python3
import sys
import argparse
import os
import json
import subprocess as sp


def get_container_info(name):
    p = sp.Popen(["docker", "inspect", name], stdout=sp.PIPE)
    stdout, stderr = p.communicate()
    result = json.loads(stdout.decode())
    return result[0]

def build_api():
    config = json.loads(open('config', 'r').read())
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
            "-v", "%s:/mnt/oj/"%(config['api']['DATA_ROOT']),
            "%s_api"%(config['prefix']),
        ]
        print(cmd)
        sp.call(cmd)

def build_web():
    pass

def build_db():
    config = json.loads(open('config', 'r').read())
    cmd = [
        "docker", "run", "-itd", "--name", "%s_db"%(config['prefix']),
    ]
    for x in config['DB']:
        cmd += ["-e", "%s=%s"%(x, config['DB'][x])]
    cmd += ["%s_db"%(config['prefix'])]
    print(cmd)
    sp.call(cmd)

def build_judge():
    pass

def build_image(name, directory):
    if sp.call(["docker", "build", "-t", name, directory]):
        print("Docker Build Broken.")
        sys.exit(1)

def build_images():
    print("=====>Building Docker...")
    config = json.loads(open('config', 'r').read())
    build_image("%s_db"%(config["prefix"]), "./db/")
    build_image("%s_api"%(config['prefix']), "./api/")
    build_image("%s_judge"%(config['prefix']), "./judge/")
    build_image("%s_web"%(config['prefix']), "./web/")
    print("=====>Docker Build Done.")

def print_config():
    config = json.loads(open('config', 'r').read())
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
    parser.add_argument("-all", help="create db api web judge", action="store_true")
    parser.add_argument("-config", help="print config", action="store_true")
    args = parser.parse_args()
    if(os.getuid() != 0):
        print("This program need root! Do you want to run it as root?(Y/n)")
        x = input().lower()
        if x == "y" or x == '':
            os.execv("/usr/bin/sudo", ["sudo", "-E",]+sys.argv)
        else:
            sys.exit(0)
    build_images()
    if args.config:
        print_config()
    if args.db:
        build_db()
    if args.api:
        build_api()


