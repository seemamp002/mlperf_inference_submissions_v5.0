| Model     | Scenario     |   Accuracy |   Throughput | Latency (in ms)   | Power Efficiency (in samples/J)   | TEST01   |
|-----------|--------------|------------|--------------|-------------------|-----------------------------------|----------|
| retinanet | multistream  |     37.334 |      1414.93 | 5.654             |                                   | passed   |
| retinanet | singlestream |     37.321 |       579.71 | 1.725             |                                   | passed   |
| retinanet | server       |     37.35  |      1414.97 | -                 |                                   | passed   |
| retinanet | offline      |     37.331 |      1733.78 | -                 |                                   | passed   |