# SNAKEMAKE at CNAG

## Set up enviroment

```bash
module load CONDA/4.5.11_PYTHON3
```

## Set up your pipeline 
Currenly are soported:
- threads
- time
- name
  
This can be set up in snakefile or cluster-config file.

**snakefile**
```
rule example1:
    input: {input}
    output: {output}
    threads: 1
    time: "10:00:00"
    name: "example1_job"
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

You must take into account, config-cluster file overwrites snakefile configuration. 

## Running a pipeline with dependencies at CNAG's cluster

```bash
snakemake --is --nt [...] \
--cluster "sbatch-cnag.py {dependencies}" \
--config "pipeline_config.json" \
--cluster-config "cluster-config.json"
```

## Writting your pipelines
Full snakemake documentation can be found [here](https://snakemake.readthedocs.io/en/stable/)