mkdir output
for path in latex/**
do
    latexSource=$path/source.tex
    directoryName=$(basename -- "$path")
    latexmk -pdf $latexSource
    mv source.pdf output/$directoryName.pdf
    rm source.*
done