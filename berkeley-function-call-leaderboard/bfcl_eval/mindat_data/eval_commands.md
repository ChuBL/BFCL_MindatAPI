## generate

bfcl generate --model gpt-4.1-2025-04-14-azure --test-category simple_python --num-threads 1

bfcl generate --model gpt-4.1-2025-04-14-azure --test-category irrelevance

## evaluate


bfcl evaluate --model gpt-4.1-2025-04-14-azure --test-category simple_python

bfcl evaluate --model gpt-4.1-2025-04-14-azure --test-category irrelevance



## mindat

bfcl generate --model gpt-4.1-2025-04-14-azure --test-category Mindat_v1

bfcl evaluate --model gpt-4.1-2025-04-14-azure --test-category Mindat_v1

bfcl evaluate --model gpt-4.1-2025-04-14-azure --test-category Mindat_v1 --partial-eval