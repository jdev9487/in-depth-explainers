mkdir output
for path in latex/**
do
    latexSource=$path/source.tex
    directoryName=$(basename -- "$path")
    pdflatex $latexSource
    mv source.pdf output/$directoryName.pdf
    rm source.aux source.log source.toc
    python3 utils/metadataWrite.py $latexSource $directoryName.pdf
done