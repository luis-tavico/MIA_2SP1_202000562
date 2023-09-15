def generarReporteDisco():
    code =  'digraph G {\n'
    code += '    subgraph cluster { margin="5.0" penwidth="1.0" bgcolor="#68d9e2"\n'
    code += '        node [style="rounded" style=filled fontname="Arial" fontsize="16" margin=0.3];\n'
    label = 'MBR|Libre\\n25% del disco|{Extendida|{EBR|Logica|EBR|Logica}}|Primaria|Libre'
    code += '        node_disk [shape="record" label="' + label + '"];\n'
    code += '    }\n'
    code += '}'

    return code

print(generarReporteDisco())