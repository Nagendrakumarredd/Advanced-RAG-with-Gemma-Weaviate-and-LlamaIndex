response = advanced_rag_query_engine.query(sample_query)
print(str(response))


print(f"Number of retrieved contexts: {len(response.source_nodes)}")

for i in range(len(response.source_nodes)):
    print(f'\nContext {i}:')
    print(response.source_nodes[i].node.text)
    print(response.source_nodes[i].node.metadata['competition_title'])



# OUTPUT

Number of retrieved contexts: 2

Context 0:
25)</li>
<li>Decoder: 1e-3</li></ul></li>
<li>Epoch: 4 (1 for warm up)</li>
<li>Batch size: 8</li>
<li>Fold: 5</li>
<li>Seed: 42</li>
</ul>
<h1>Parameters</h1>
<ul>
<li>Backbone: deberta-v3-base, deberta-v3-large, deberta-v3-small</li>
<li>Pooling: mean, cls, max,
Feedback Prize - English Language Learning

Context 1:
My best CV score is 0.4484.</p>
<h1>Best Model Configuration</h1>
<ul>
<li>Backbone: deberta-v3-base</li>
<li>Pooling: mean</li>
<li>Max_len: 512</li>
<li>Learning rate:<ul>
<li>Encoder: 2e-4 (layer-wise lr decay: 0.
Feedback Prize - English Language Learning

