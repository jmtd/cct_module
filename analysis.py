#!/usr/bin/python3
# module use analysis

import yaml
import os
from collections import defaultdict

mods={} # name: [implementations as yaml]

def deps(n,v,done=defaultdict(lambda: 1)):
    """output the modules that input module depends upon, recursively
    """
    if (n,v) in done:
        return
    done[(n,v)] = 1

    for dep in mods[n]:
        for d in dep.get('modules',{}).get('install',[]):
            if 'version' in d:
                deps(d['name'],d['version'],done)
            else:
                # figure out what versions there are
                for impl in mods[d['name']]:
                    deps(impl['name'],impl['version'],done)

    return done

def populateMods():
    """read in all module definitions and populate the mods hash
    (module name -> [list of implementations])
    """
    for (x,y,z) in os.walk("."):
        if "module.yaml" in z:
            f=os.path.join(x,"module.yaml")
            s=yaml.load(open(f).read())
            n=s['name']
            if not n in mods:
                mods[n]=[]
            mods[n].append(s)

if __name__=="__main__":
    y="/home/jon/git/rh/images/redhat-openjdk-18-openshift-image/image.yaml"
    populateMods()
    i=yaml.load(open(y).read())
    mods[i['name']] = [i]
    print("{}, version {}".format(i['name'],i['version']))

    d = list(deps(i['name'],i['version']).keys())
    print("{} dependencies ({})".format(len(d),d))

    i = 0
    for impls in mods.values():
        i += len(impls)
    print("{} total modules, really".format(i))
