*Check [CM MLPerf docs](https://docs.mlcommons.org/inference) for more details.*

## Host platform

* OS version: Linux-6.8.0-53-generic-x86_64-with-glibc2.39
* CPU version: x86_64
* Python version: 3.12.3 (main, Jan 17 2025, 18:03:48) [GCC 13.3.0]
* MLC version: unknown

## CM Run Command

See [CM installation guide](https://docs.mlcommons.org/inference/install/).

```bash
pip install -U mlcflow

mlc rm cache -f

mlc pull repo mlcommons@mlperf-automations --checkout=e98137ebbf4a43eef6c2f13de79e47324f6346f9


```
*Note that if you want to use the [latest automation recipes](https://docs.mlcommons.org/inference) for MLPerf,
 you should simply reload mlcommons@mlperf-automations without checkout and clean MLC cache as follows:*

```bash
mlc rm repo mlcommons@mlperf-automations
mlc pull repo mlcommons@mlperf-automations
mlc rm cache -f

```

## Results

Platform: mini-ctuning_cpp_tflite-cpu-tflite_vmaster-default_config

Model Precision: fp32

### Accuracy Results 
`acc`: `71.678`, Required accuracy for closed division `>= 75.6954`

### Performance Results 
`90th percentile latency (ns)`: `13597829.0`
