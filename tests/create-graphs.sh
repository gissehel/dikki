for basename in graph graph-point graph-all graph-point-all ; do 
    dot -Tpng < ${basename}.output > ../doc/${basename}.png
done
