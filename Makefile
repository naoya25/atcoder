# 提出コードの集計してログを取る
log:
	python submissions/aggregate_submission.py

# ワイルドカード: make {dir_name}
%:
	@python make_dir.py $@
