#convert screenshot.png \
#\( +clone -fuzz 25% -fill black +opaque "#F23C32" -fill white -opaque "#832525" \) \
#-alpha off -compose copy_opacity -composite output.png
convert screenshot.png -fuzz 30% -fill white +opaque "#F23C32" -fill white +opaque "#832525" output.png
