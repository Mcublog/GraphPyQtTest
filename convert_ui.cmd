pyrcc5 %~dp0ui\res\res.qrc 	-o %~dp0ui\res_rc.py
pyuic5 %~dp0ui\graph_test.ui 	-o %~dp0ui\graph_test.py
pyuic5 %~dp0ui\select_dialog\select_graph.ui 	-o %~dp0ui\select_dialog\select_dialog.py
pyuic5 %~dp0ui\select_dialog\select_journal.ui 	-o %~dp0ui\select_dialog\select_journal.py