#!/usr/bin/env bash
##############################################################################
# Genera la documentacion de los modulos, requiere la instalacion de oca
# maintainers tools en tu maquina.
# bajalo de aca --> https://github.com/OCA/maintainer-tools
#
source /home/jobiols/.virtualenvs/oca/bin/activate
oca-gen-addon-readme \
	--org-name jobiols \
	--repo-name cl-cooperativas \
	--branch 9.0 \
	--addons-dir "$PWD" \
	--gen-html
