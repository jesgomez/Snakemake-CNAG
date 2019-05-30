#!/usr/bin/env python3
import os
import sys 

from snakemake.utils import read_job_properties

jobscript = sys.argv[-1]  
dependencies = set(sys.argv[1:-1])

cmdline = ["sbatch"]

if dependencies:
    cmdline.append("--dependency")
    cmdline.append( "afterok:" + ",".join(dependencies))
job_properties = read_job_properties(jobscript)

cpus = job_properties.get("threads","1")
if 'threads' in job_properties["cluster"]:
	cpus = job_properties["cluster"]["threads"]

time = job_properties.get("time", "10:00:00")
if "time" in job_properties['cluster']:
	time = job_properties['cluster']["time"]

name = job_properties.get("name", "Snakejob")
if "name" in job_properties['cluster']:
	name = job_properties['cluster']["name"]


cmdline.append("--parsable --job-name={name} --time={time} --cpus-per-task={cpus}".format(time=time, cpus=cpus,name=name))
cmdline.append(jobscript)

# Constructs and submits
cmdline = " ".join(cmdline)
os.system(cmdline)
