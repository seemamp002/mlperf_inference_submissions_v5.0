| Model     | Scenario     |   Accuracy |   Throughput | Latency (in ms)   | Power Efficiency (in samples/J)   | TEST01   |
|-----------|--------------|------------|--------------|-------------------|-----------------------------------|----------|
| retinanet | server       |     37.317 |      637.538 | -                 |                                   | passed   |
| retinanet | multistream  |     37.283 |      732.936 | 10.915            |                                   | passed   |
| retinanet | offline      |     37.344 |      862.338 | -                 |                                   | passed   |
| retinanet | singlestream |     37.34  |      572.738 | 1.746             |                                   | passed   |