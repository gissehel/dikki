for basename in images-graph images-graph-point images-graph-all images-graph-point-all ; do 
    dot -Tpng < ${basename}.output > ../doc/${basename}.png
done
