#!/bin/bash
cgroupfs_mount() {
    if grep -v '^#' /etc/fstab | grep -q cgroup \
        || [ ! -e /proc/cgroups ] \
        || [ ! -d /sys/fs/cgroup ]; then
        return
    fi
    if ! mountpoint -q /sys/fs/cgroup; then
        mount -t tmpfs -o uid=0,gid=0,mode=0755 cgroup /sys/fs/cgroup
    fi
    (
        cd /sys/fs/cgroup
        for sys in $(awk '!/^#/ { if ($4 == 1) print $1 }' /proc/cgroups); do
            mkdir -p $sys
            if ! mountpoint -q $sys; then
                if ! mount -n -t cgroup -o $sys cgroup $sys; then
                    rmdir $sys || true
                fi
            fi
        done
    )
}
if [ ! -d "/nctuoj_contest_judge" ]; then
    set -e
    if [ "$BASE_URL" = "" ]; then
        BASE_URL="172.17.0.1"
    fi
    git clone https://github.com/Tocknicsu/nctuoj_contest_judge.git
    cd nctuoj_contest_judge
    cp config.py.sample config.py
    echo "base_url = \"$BASE_URL\"" >> config.py
else
    cd /nctuoj_contest_judge
    git pull --rebase
fi
cgroupfs_mount
cd /nctuoj_contest_judge
pip3 install --upgrade -r requirements.txt
python3 judge.py
# docker run -itd --privileged --name oj_judge_client --link oj_judge_center:oj_judge_center -e judgecenter_host=oj_judge_center -P -v /mnt/nctuoj:/mnt/nctuoj judge_client
# --privileged 是為了讓container有權限mount cgroupfs才能跑isolate
