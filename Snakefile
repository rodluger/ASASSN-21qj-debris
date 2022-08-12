rule proc_atlas:
     input:
        "job211831.txt"
     output:
        "obs_ATLAS.ecsv"
     conda:
        "environment.yml"
     script:
        "src/scripts/convert_atlas.py"