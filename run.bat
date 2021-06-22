rem pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ 
rem pytest -s -v -m "sanity or regression" --html=./Reports/report.html testCases/ 
rem pytest -s -v -m "regression" and regression" --html=./Reports/report.html testCases/ 
pytest -s -v -m "sanity" --html=./Reports/report.html testCases/