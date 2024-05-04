convert screenshot.png \
\( +clone -fuzz 31% -fill black +opaque "#F23C32" -fill white -opaque "#832525" \) \
-alpha off -compose copy_opacity -composite output.png
