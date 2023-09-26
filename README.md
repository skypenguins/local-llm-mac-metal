# llama-cpp-python on Mac with Metal (MPS)
llama.cppのPythonバインディングである[llama-cpp-python](https://github.com/abetlen/llama-cpp-python)を、Macで試す。
CPUだと遅いので、Metalで推論を高速化する。

# Prerequisites
* macOS Ventura 13.6
* Xcode Command Line Tools
* HomeBrew 4.1.13
* Python 3.11.5
* Poetry 1.6.1

# llama-cpp-pythonのインストール
1. `poetry init`
2. `POETRY_CMAKE_ARGS="-DLLAMA_METAL=on" poetry add llama-cpp-python`

# モデルのダウンロード
GGUF形式のモデルを使う。

* https://huggingface.co/TheBloke/Yarn-Llama-2-7B-64K-GGUF
* https://huggingface.co/TheBloke/Yarn-Llama-2-13B-64K-GGUF
* https://huggingface.co/mmnga/line-corp-japanese-large-lm-3.6b-instruction-sft-gguf
