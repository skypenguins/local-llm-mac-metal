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

# text-generation-webui
1. `git clone https://github.com/oobabooga/text-generation-webui.git`
2. `cd text-generation-webui`
3. `poetry init`
4. `requirements_apple_silicon.txt` を本dirのやつに置き換え。
5. `poetry add $( cat requirements_apple_silicon.txt )`
6. `POETRY_CMAKE_ARGS="-DLLAMA_METAL=on" poetry add llama-cpp-python`
7. `poetry run python server.py --model-dir path/to/model` で起動。
8. `http://127.0.0.1:7860/` にブラウザでアクセス。
9. modelタブでllama.cppを選択し、適宜モデルを選ぶ。
10. Loadを押して、モデルを読み込む。
