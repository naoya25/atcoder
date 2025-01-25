# 提出コードの集計してログを取る
log:
	python system/make_log.py

# ワイルドカード: make {dir_name}
%:
	@python system/make_dir.py $@
