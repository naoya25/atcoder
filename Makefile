# 提出コードの集計
sub:
	python submissions/aggregate_submission.py

# ワイルドカード: make {dir_name}
%:
	@python make_dir.py $@
