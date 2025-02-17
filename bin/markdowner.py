#!/usr/local/bin/python3

import inspect, json, sys, re, yaml
from os import getlogin, makedirs, pardir, path, system
from pathlib import Path
from json_ref_dict import RefDict, materialize

dir_path = path.dirname( path.abspath(__file__) )

from bycon import * #BYC, read_schema_file
import byconServices

################################################################################

def main():
    """
    This is a very specific script to generate markdown files from yaml files.
    Don't look at the code.
    """

    schemas_yaml_path = path.join( dir_path, pardir, "src", "requests")
    examples_yaml_path = path.join( schemas_yaml_path, "examples")
    generated_docs_path = path.join( dir_path, pardir, "docs", "generated")

    # external_documantation_path = path.abspath(path.join( dir_path, pardir, pardir, "variant-query-types", "docs", "generated"))

    #>------------------------------------------------------------------------<#

    """

    """



    file_pars = {
        "requestParameterComponents":{
            "headline": "Request Parameter Definitions",
            "root": "$defs"
        },
        "requestProfiles": {
            "headline": "Request Profile Definitions",
            "root": "$defs"
        }
    }

    request_pattern_ids = {}
    schemas = {}

    for d_k, d_v in file_pars.items():
        ofp = path.join(schemas_yaml_path, f'{d_k}.yaml' )
        with open(ofp) as od:
            schemas.update({d_k: yaml.load(od, Loader=yaml.FullLoader)})

        pp_f = path.join(generated_docs_path, f"{d_k}.md")

        ls = [f'# {d_v.get("headline")}']

        ls.append(f'\n{schemas[d_k].get("description", "")}\n')

        r_k = d_v.get("root","$defs")

        pp = schemas[d_k].get(r_k, {})
        for pk, pi in pp.items():

            # very special
            if d_k == "requestProfiles":
                request_pattern_ids.update({pk: pi.get("description", "")})

            ls.append(f'## `{pk}` \n')
            ls = __add_md_parameter_lines(ls, pi)

        pp_fh = open(pp_f, "w")
        pp_fh.write("\n".join(ls).replace("\n\n", "\n").replace("\n\n", "\n").replace("\n#", "\n\n#"))
        pp_fh.close()

    #>------------------------------------------------------------------------<#

    skips = []
    ph = "g_variant"
    gv_f = path.join(generated_docs_path, f"requestProfiles_{ph}.md")
    gv_fh = open(gv_f, "w")
    gv_fh.write(f'# Beacon v2 Requests\n\n{request_pattern_ids.get(ph, "")}\n\n')
    gv_fh.write(f'\nFor the parameter definitions please see the [`requestParameterComponents` page.](../requestParameterComponents/)\n\n')
    gv_fh.write(f'## {ph} Parameters\n\n')
    ls = []
    ls = __add_md_def_lines(ls, schemas["requestProfiles"]["$defs"][ph]["properties"])
    gv_fh.write("\n".join(ls).replace("\n\n", "\n").replace("\n\n", "\n").replace("\n#", "\n\n#"))
    gv_fh.write(f'\n\n## Beacon v2 Request Examples\n\n')
    skips.append(ph)

    ph = "VQSrequest"
    vqs_f = path.join(generated_docs_path, f"requestProfiles_{ph}.md")
    vqs_fh = open(vqs_f, "w")
    vqs_fh.write(f'# Beacon VQS Requests\n\n{request_pattern_ids.get(ph, "")}\n\n')
    vqs_fh.write(f'\nFor the parameter definitions please see the [`requestParameterComponents` page.](../requestParameterComponents/)\n\n')
    vqs_fh.write(f'## {ph} Parameters\n\n')
    ls = []
    ls = __add_md_def_lines(ls, schemas["requestProfiles"]["$defs"][ph]["properties"])
    vqs_fh.write("\n".join(ls).replace("\n\n", "\n").replace("\n\n", "\n").replace("\n#", "\n\n#"))
    vqs_fh.write(f'\n\n## Beacon v2+/VQS "VRSified" Request Examples\n\n')
    skips.append(ph)

    for rp_id, rp_desc in request_pattern_ids.items():
        if rp_id in skips:
            continue
        rp_f = path.join(generated_docs_path, f"requestProfiles_{rp_id}.md")
        rp_fh = open(rp_f, "w")
        rp_fh.write(f'# Request Profile: `{rp_id}`\n\n{rp_desc}')

        ex_f = path.join(examples_yaml_path, f"{rp_id}.yaml")

        if path.exists(ex_f):
            with open(ex_f) as ex_fh:
                ex_d = yaml.load(ex_fh, Loader=yaml.FullLoader)
                ex_ls = [f'## `{rp_id}` Examples']
                for ex_id, ex in ex_d["examples"].items():
                    rp_fh.write(f'\n\n{ex.get("description", "")}\n')
                    if "BV2" in rp_id:
                        gv_fh.write(f'\n\n{ex.get("description", "")}\n')
                    elif "VQS" in rp_id:
                        vqs_fh.write(f'\n\n{ex.get("description", "")}\n')
                    rq = ex.get("request", {})
                    ls = []
                    ls.append(f'#### Request \n')
                    ls = __add_md_parameter_lines(ls, rq)
                    ls.append(f'\n##### GET query string\n```{__request_make_GET(rq)}```\n')
                    ls.append(f'\n##### POST query component \n```{__request_make_POST(rq)}```\n')
                    rp_fh.write("\n".join(ls).replace("\n\n", "\n").replace("\n\n", "\n").replace("\n#", "\n\n#"))
                    if "BV2" in rp_id:
                        gv_fh.write("\n".join(ls).replace("\n\n", "\n").replace("\n\n", "\n").replace("\n#", "\n\n#"))
                    elif "VQS" in rp_id:
                        vqs_fh.write("\n".join(ls).replace("\n\n", "\n").replace("\n\n", "\n").replace("\n#", "\n\n#"))

        rp_fh.close()
    gv_fh.close()
    vqs_fh.close()

    # cmd = f'rsync -avh --delete {generated_docs_path}/ {external_documantation_path}/'
    # print(cmd)

    # system(f'rsync -avh --delete {generated_docs_path}/ {external_documantation_path}/')


################################################################################

def __request_make_GET(rq):
    pars = []
    for k, v in rq.items():
        if type(v) is list:
            pars.append(f'{k}={",".join(str(x) for x in v)}')
        else:
            pars.append(f'{k}={v}')
    return f'{"&".join(pars)}'

################################################################################

def __request_make_POST(rq):
    return json.dumps(rq, indent=4, sort_keys=True, default=str)

################################################################################

def __add_md_def_lines(lines, parameter):
    for pik, piv in parameter.items():
        if (f_l := __reformat_ref(pik, piv)):
            lines += f_l

    return lines

################################################################################

def __add_md_parameter_lines(lines, parameter):

    for pik, piv in parameter.items():
        # print(f'{pik}: {type(piv)}')
        if type(piv) is dict:
            if (f_l := __reformat_ref(pik, piv)):
                lines += f_l
                return lines
            js = '  \n'
            lines.append(f'* `{pik}`:    \n')
            lines.append(js.join([f'    - `{k}`: `{str(v).replace("{", "").replace("}", "")}`    ' for k, v in piv.items()]))                    
        elif type(piv) is list:
            js = '`    \n    - `'
            piv = f'    \n    - `{js.join([str(x).replace("{", "").replace("}", "").replace("'", "") for x in piv])}`    '
            lines.append(f'    \n* `{pik}`: {piv}    ')
        elif "default" in pik or "pattern" in pik and len(str(piv)) > 0:
            lines.append(f'    \n* `{pik}`: `{piv}`    ')
        elif "description" in pik:
            lines.append(f'#### Description\n')
            piv = piv.replace("*", "    \n*")
            lines.append(f'{piv}    \n#### Definitions\n')
        else:
            lines.append(f'    \n* `{pik}`: `{piv}`    ')
        lines.append(f'\n')

    return lines

def __reformat_ref(pik, piv):
    if not (p_ref := piv.get("$ref")):
        return
    p_link = p_ref.replace("./requestParameterComponents.yaml", "../requestParameterComponents")
    p_link = p_link.replace("/$defs/", "")
    p_base, p_rest = p_link.split('#')
    return [f'    \n#### `{pik}`: [{p_ref}]({p_base}#{p_rest.lower()})    ']


################################################################################
################################################################################
################################################################################

if __name__ == '__main__':
    main()
