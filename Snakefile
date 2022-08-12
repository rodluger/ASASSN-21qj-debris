rule proc_atlas:
     input:
        "job211831.txt"
     output:
        "obs_ATLAS.ecsv"
     conda:
        "environment.yml"
     script:
        "src/scripts/convert_atlas.py"
rule proc_asassn:
     input:
        "light_curve_f51db35b-11b8-4840-a6d9-979a455d6978.csv"
     output:
        "obs_ASASSN.ecsv"
     conda:
        "environment.yml"
     script:
        "src/scripts/convert_asassn.py"

rule proc_neowise:
     input:
        "ASASSN-21qj_2013-2021.tbl"
     output:
        "obs_NEOWISE.ecsv"
     conda:
        "environment.yml"
     script:
        "src/scripts/convert_neowise.py"
