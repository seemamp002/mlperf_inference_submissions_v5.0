*Check [CM MLPerf docs](https://docs.mlcommons.org/inference) for more details.*

## Host platform

* OS version: Linux-5.15.167.4-microsoft-standard-WSL2-x86_64-with-glibc2.35
* CPU version: x86_64
* Python version: 3.10.12 (main, Jan 17 2025, 14:35:34) [GCC 11.4.0]
* MLC version: unknown

## CM Run Command

See [CM installation guide](https://docs.mlcommons.org/inference/install/).

```bash
pip install -U mlcflow

mlc rm cache -f

mlc pull repo mlcommons@mlperf-automations --checkout=dd6f2a8a79de14ae7d9c435ba7a70e696de81e58


```
*Note that if you want to use the [latest automation recipes](https://docs.mlcommons.org/inference) for MLPerf,
 you should simply reload mlcommons@mlperf-automations without checkout and clean MLC cache as follows:*

```bash
mlc rm repo mlcommons@mlperf-automations
mlc pull repo mlcommons@mlperf-automations
mlc rm cache -f

```

## Results

Platform: 53e8ba3f30a3-reference-cpu-onnxruntime_v1.20.1-default_config

Model Precision: fp32

### Accuracy Results 
`acc`: `76.456`, Required accuracy for closed division `>= 75.6954`

### Performance Results 
`90th percentile latency (ns)`: `21784200.0`
