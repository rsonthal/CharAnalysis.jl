{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "TreeEmbeddings.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyN//gmBxpX0i47bZolcvCTc",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/rsonthal/CharAnalysis.jl/blob/master/rsonthal_xfcui/TreeRep.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "id": "hJxl-JMnhB-x"
      },
      "outputs": [],
      "source": [
        "import networkx as nx\n",
        "import geomstats.backend as gs"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import TreeRep"
      ],
      "metadata": {
        "id": "249LAcQIhJLl",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d1e07c7f-5436-40bb-ceb8-faaf5be706d5"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "INFO: Using numpy backend\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from importlib import reload \n",
        "reload(TreeRep)\n",
        "\n",
        "for trial in range(100,5000,100):\n",
        "  n = 200\n",
        "  G = nx.gnp_random_graph(200, 0.7)\n",
        "  for e in G.edges():\n",
        "      G[e[0]][e[1]]['weight'] = gs.random.rand()*10\n",
        "  d = nx.algorithms.shortest_paths.dense.floyd_warshall(G)\n",
        "  D = gs.zeros((n,n))\n",
        "  for i in range(n):\n",
        "    for j in range(n):\n",
        "      D[i,j] = d[i][j]\n",
        "\n",
        "  T = TreeRep.TreeRep(D)\n",
        "  T.learn_tree()\n",
        "  print(G.number_of_nodes(), G.number_of_edges())\n",
        "  print(T.G.number_of_nodes(),T.G.number_of_edges())\n",
        "  print(nx.is_k_edge_connected(T.G,1), nx.is_k_edge_connected(T.G,2))\n",
        "  print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 664
        },
        "id": "q7DkIMMkjqSn",
        "outputId": "2cc92c9f-4658-486c-bd24-e00f8c63cb63"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "200 13870\n",
            "289 288\n",
            "True False\n",
            "\n",
            "200 13941\n",
            "271 270\n",
            "True False\n",
            "\n",
            "200 13917\n",
            "273 272\n",
            "True False\n",
            "\n",
            "200 13873\n",
            "297 296\n",
            "True False\n",
            "\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-9-92aabcb869cf>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      7\u001b[0m   \u001b[0;32mfor\u001b[0m \u001b[0me\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mG\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0medges\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m       \u001b[0mG\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0me\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0me\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'weight'\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mgs\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrandom\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrand\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0;36m10\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 9\u001b[0;31m   \u001b[0md\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnx\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0malgorithms\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mshortest_paths\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdense\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfloyd_warshall\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mG\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     10\u001b[0m   \u001b[0mD\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mgs\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mzeros\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mn\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mn\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     11\u001b[0m   \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mn\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/networkx/algorithms/shortest_paths/dense.py\u001b[0m in \u001b[0;36mfloyd_warshall\u001b[0;34m(G, weight)\u001b[0m\n\u001b[1;32m    231\u001b[0m     \"\"\"\n\u001b[1;32m    232\u001b[0m     \u001b[0;31m# could make this its own function to reduce memory costs\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 233\u001b[0;31m     \u001b[0;32mreturn\u001b[0m \u001b[0mfloyd_warshall_predecessor_and_distance\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mG\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mweight\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mweight\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/networkx/algorithms/shortest_paths/dense.py\u001b[0m in \u001b[0;36mfloyd_warshall_predecessor_and_distance\u001b[0;34m(G, weight)\u001b[0m\n\u001b[1;32m    150\u001b[0m             \u001b[0;32mfor\u001b[0m \u001b[0mv\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mG\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    151\u001b[0m                 \u001b[0md\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mdist_u\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mw\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0mdist_w\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mv\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 152\u001b[0;31m                 \u001b[0;32mif\u001b[0m \u001b[0mdist_u\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mv\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m>\u001b[0m \u001b[0md\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    153\u001b[0m                     \u001b[0mdist_u\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mv\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0md\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    154\u001b[0m                     \u001b[0mpred\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mu\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mv\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpred\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mw\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mv\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: "
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# New Section"
      ],
      "metadata": {
        "id": "3jcEz9KurLb5"
      }
    }
  ]
}