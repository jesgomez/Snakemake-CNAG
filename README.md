# SNAKEMAKE at CNAG

## Set up enviroment
Get snakemake >= 6.0.5 and python3 in your environment. This script has been tested with Snakemake v6.0.5

## Set up your pipeline 
Currently sopported:
- threads
- time
- name
- qos
- partition
- constraint
- array
  
These can be set up in snakefile or cluster-config file.

**snakefile**
```
rule example1:
    input: {input}
    output: {output}
    threads: 1
    params:
        time = "10:00:00"
        name = "JobName" 
```

**cluster-config.json**

```json
{
    "example1":
        {
            "name": "example1_job",
            "time": "23:00:00",
            "threads": 2
        }
}

```
If one of the rules uses wildcards, you can specify a different jobname per wildcard (eg. using the wildcard "file"): 

```json
{
    "example1":
        {
            "name": "example1_job.{wildcards.file}",
            "time": "23:00:00",
            "threads": 2
        }
}

```

You must take into account, config-cluster file overwrites snakefile configuration. 

## Running a pipeline with dependencies at CNAG's cluster

```bash
snakemake --jobs 999 --is --nt [...] \
--snakefile "mySnakeFile" \
--cluster "sbatch-cnag.py {dependencies}" \
--config "pipeline_config.json" \
--cluster-config "cluster-config.json"
```

## Writing your pipelines
Full snakemake documentation can be found [here](https://snakemake.readthedocs.io/en/stable/)
