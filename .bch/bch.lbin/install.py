#!/usr/bin/env python3
from pathlib import Path
from myborg.lbin.main import copyall
modroot = Path(__file__).parent.parent.parent
src = modroot/'lbin.app'
print(src)
copyall( src )
