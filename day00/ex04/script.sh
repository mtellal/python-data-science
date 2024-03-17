#!/bin/bash

echo "Testing whatis.py"

whatis() {
        echo -e "\npython whatis.py $@"
        python whatis.py $@
}


whatis 14
whatis -5
whatis
whatis 0
whatis Hi!
whatis 13 5
whatis 65465464654654654654653
whatis 65465464654654654654654
whatis -1
whatis whatis.py
whatis +14
whatis ++13
whatis -13
whatis --13
