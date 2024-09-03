from transformers import pipeline
unmasker = pipeline('fill-mask', model='bert-base-uncased')
print(unmasker("The city of [MASK] is the capital of Tonga."))