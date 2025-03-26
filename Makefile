help: ## ヘルプを表示します。
	@echo 'targetを下記から指定して実行してください'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'


log: ## 提出コードの集計してログを取る
	python system/make_log.py


%: ## ワイルドカード: make {dir_name}
	@python system/make_dir.py $@
