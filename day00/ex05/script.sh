#!/bin/bash

set -x

python building.py ""
echo -e "\n"

python building.py "\\"
echo -e "\n"

python building.py "wdjf wdfjb wpibf wpif w"
echo -e "\n"

python building.py "Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."
echo -e "\n"

python building.py "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sagittis sit amet tortor a cursus. In non tristique ligula. Donec commodo, odio vitae tincidunt blandit, tortor mauris egestas ligula, et faucibus est est et nibh. Maecenas egestas aliquam varius. Nulla sollicitudin tempor urna ut accumsan. Morbi non augue sagittis, sodales tortor in, placerat nulla. Aenean non est id mauris facilisis tristique vitae et sem. Sed dignissim tortor quis ex blandit, a suscipit dui faucibus. Morbi urna augue, tincidunt at egestas eu, scelerisque vel metus. Nunc ac metus turpis.

Quisque feugiat vitae tellus sit amet venenatis. Aenean quam nisi, gravida vitae diam a, ornare iaculis libero. Nunc commodo nisi non sapien mattis elementum. Praesent vehicula scelerisque lectus ornare viverra. Duis nec pharetra velit. Cras euismod justo eu fringilla imperdiet. Proin cursus ipsum in lorem malesuada pellentesque. Nullam at eros fringilla dui euismod interdum id sit amet quam. Donec vitae vulputate quam, eget dictum libero. Vivamus pellentesque congue nisl in sagittis. Morbi bibendum lectus sapien, quis hendrerit purus iaculis quis. Proin tincidunt, nisl vel porta iaculis, ligula odio mattis leo, sit amet euismod est quam et nunc.

Cras feugiat, enim quis lobortis laoreet, est sapien finibus augue, iaculis luctus velit nulla vitae magna. Donec elementum gravida feugiat. Nulla facilisi. Aenean aliquam velit sed pellentesque pharetra. Nulla hendrerit rutrum pharetra. Nulla facilisi. Nam sit amet bibendum nisi. Duis fermentum lectus eu massa semper faucibus. Ut vestibulum arcu nibh, a faucibus nulla condimentum eget.

Etiam malesuada mauris vitae tincidunt rhoncus. Aenean quis lectus quis nisl ultrices bibendum ac quis ante. Pellentesque posuere augue nec justo laoreet, et ullamcorper nibh accumsan. Nunc eget aliquam eros. Phasellus cursus erat eu sagittis dignissim. Duis sodales tempor sollicitudin. Morbi nec justo magna. Curabitur nunc nibh, pretium facilisis egestas eget, tempus ut est. Integer a laoreet purus.

Proin volutpat felis id augue mollis bibendum. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam ut tortor dapibus, suscipit justo id, vestibulum turpis. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed tristique vel leo nec efficitur. Morbi suscipit metus ac enim tempus, in faucibus sapien dapibus. Phasellus in dictum enim. Etiam at consectetur dolor."

echo -e "\n"
echo "" | python building.py

echo -e "\n"
echo "Hello World!" | python building.py

echo -e "\n"
echo "wdfwdf wdfw wf" | python building.py
