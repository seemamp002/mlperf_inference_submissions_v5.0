| Model    | Scenario     |   Accuracy |   Throughput | Latency (in ms)   | Power Efficiency (in samples/J)   | TEST01   | TEST04   |
|----------|--------------|------------|--------------|-------------------|-----------------------------------|----------|----------|
| resnet50 | server       |     76.078 |     35342.5  | -                 |                                   | passed   | passed   |
| resnet50 | multistream  |     76.064 |     17057.6  | 0.469             |                                   | passed   | passed   |
| resnet50 | offline      |     76.078 |     43783.8  | -                 |                                   | passed   | passed   |
| resnet50 | singlestream |     76.064 |      3597.12 | 0.278             |                                   | passed   | passed   |