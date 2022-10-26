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

time = job_properties['params'].get("time", "10:00:00")
if "time" in job_properties['cluster']:
	time = job_properties['cluster']["time"]

name = job_properties["params"].get("name", "Snakejob")
if "name" in job_properties['cluster']:
	name = job_properties['cluster']["name"]

queue = job_properties.get("queue", "genD")
if "queue" in job_properties['cluster']:
	queue = job_properties['cluster']["queue"]

qos = job_properties.get("qos", "normal")
if "qos" in job_properties['cluster']:
	qos = job_properties['cluster']["qos"]

mem = job_properties.get("mem", "100")
if "mem" in job_properties['cluster']:
        mem = job_properties['cluster']['mem']

constraint = job_properties.get("constraint", "")
if "constraint" in job_properties['cluster']:
	constraint = job_properties['cluster']["constraint"]

array= job_properties.get("array", "")
if "array" in job_properties['cluster']:
        array = job_properties['cluster']["array"]
        error = job_properties.get("error","logs/slurm-%A_%a.err")
        out = job_properties.get("out","logs/slurm-%A_%a.out")      
else:
        log = job_properties.get("log","slurm-%j.out")
        if "log" in job_properties['cluster']:
                log = job.properties['cluster']["log"]
        out = log[0]
        error = log[1]

cmdline.append("--parsable --job-name={name} --error={error} --output={out} --time={time} --partition={queue} --qos={qos} --cpus-per-task={cpus} --constraint={constraint} --mem={mem} --array={array}".format(time=time, cpus=cpus,name=name,queue=queue, qos=qos, error=error, out=out, constraint=constraint, array=array, mem=mem))
cmdline.append(jobscript)
cmdline = " ".join(cmdline)
os.system(cmdline)
# Constructs and submits


