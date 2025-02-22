# Biopython
biopython은 파이썬 기반 컴퓨터 분자 생물학 파이썬 라이브러리이다. 생물정보학 분야에서 자주 사용되며, DNA, RNA, 단백질 서열 데이터 및 생물학 관련 다양한 데이터 형식들을 다룰 수 있는 도구를 제공한다.

- 기능
    - 서열 분석
        - DNA, RNA, Proten sequence.
        - GC 함량 계산, 역상보 서열 생성 등의 작업 가능
    - 파일 포맷 피싱
        - 여러 생물정보학 파일 포멧을 파이썬 데이터 구조로 지원한다.
        - Blast output, Clustalw, FASTA, GenBank, PubMed and Medline, ExPASy files, SCOP, UniGene, SwisssProt
    - 생물학적 데이터 접근
        - NCBI, UniProt 등 외부 데이터베이스와의 연결할 수 있다.
        - BLAST 검색 자동화 가능하다.
    - 계보 및 진화 분석
        - 계통도 생성 및 분석을 위한 도구가 포함되어 있다.
        - Phylo 모듈로 다양한 포맷의 계통수를 다룬다.
    - 알고리즘 및 분석 도구
        - Smith-Waterman, Needleman-Wunsch 등의 정렬 알고리즘 구현한다.
        - 서열 간의 유사성 계산, 정렬 작업 가능하다.
    - 구조 데이터 처리
        - 단백질 구조 데이터를 PDB 포맷으로 파싱 및 분석 가능하다.

# Chapter 01 시퀀싱 객체
생물학적 시퀀싱은 생물정보학의 중요한 객체이며, 이번 챕터에서 시퀀싱를 처리하기 위해 Biopython 매커니즘인 `Sep`객체를 소개한다.

시퀀싱은 근본적으로 문자열이며 `AGTACACTGGT`처럼, 이는 생물학적 파일 형식에서 시퀀스를 보는 가장 일반적인 방식이기 때문에 매우 자연스럽게 보인다.

객체와 표준 Python 문자열의 가장 중요한 차이점은 `Seq`와 서로 다른 메서드가 있다. `Sep`객체는 일반 문자열과 동일한 메서드 중 많은 것을 지원 하지만, `translate()`메서드는 생물학적 번역을 수행하여 다르며, 생물학적으로 관련된 추가 메서드 `reverse_complement()` 메서드도 존재한다.

### Sep()
-> 시퀀스 객체를 만드는 메서드

### .count()을 이용한 개수 카운트
`Seq`는 파이썬에서 사용하는 .count()을 이용할 수 있다. 이는 문자열 및 리스트 객체에서 사용되는 메서드로, 특정 요소나 값이 등장하는 횟수를 반환한다.

- 기본 문법
    `string.count(sub, strart=0, end=len(string))`
    - sub : 찾고자 하는 부분 문자열
    - strart(선택) : 검색을 시작할 인덱스 (기본값: 0)
    - end(선택) : 검색을 종료할 인덱스 (기본값: len(string))

### Bio.SeqUtils, GC% 함수
DNA에서 GC%(구아닌, 사이토신 비율)은 생물학적, 진화적, 그리고 실험적 관점에서 중요한 의미를 갖는다. GC 함량은 유전자의 구조적, 기능적 특징뿐만 아니라 생물 종의 적응과 환경 변화에 대한 반응을 이해하는 데에도 유용하다.

- GC%의 정의

	GC%: DNA 서열에서 **구아닌(G)**과 **사이토신(C)**이 전체 염기쌍에서 차지하는 비율.

    GC\% = \frac{\text{G의 개수} + \text{C의 개수}}{\text{총 염기쌍 수}} \times 100

- 중요성
    1. 유전자 안정성과 구조
        - G와 C는 3개의 수소 결합을 형성하는 반면, A와 T은 2개의 수소 결합만 형성한다. 그렇기에 GC 함량이 높을수록 DNA는 더 안정적이며, 특히 고온 환경에서 쉽게 변성되지 않는다.
        - GC는 DNA의 녹는점에 영향을 줌
            - Tm : DNA가 이중나선 구조에서 단일 가닥으로 분리되는 온도 -> GC 증가 = Tm 증가
    2. 진화적, 환경적 적응
        - 고온 환경에 서식하는 생물의 DNA는 GC함량이 높은 경향이 있다.
        - 특정 생물 종이나 유전자 집합의 진화적 적응과 밀접하게 관련된다.
    3. 유전자 발현 조절
        - 프로모터와 같은 조절 서열에서 CpG 섬이 종종 발견된다.
            - CpG 섬은 유전자 발현 조절과 관련 있으며, 특정 유전자의 활성화 여부에 영향을 미친다.
            - ex : 포유류에서 CpG 메틸화는 유전자 발현 억제와 연관됨
    4. 서열 분석 및 유전자 특징
        - GC 함량은 생물의 게놈 특징을 나타냄
            - 세균과 같은 생물에서 GC는 유전체의 특정 영역의 기능적 차이를 암시
        - GC 함량이 낮거나 높은 영역은 종종 특정 기능(예: 유발 유전자)이나 구조적 역할과 연관
    5. 실험적 중요성
        - PCR 실험에서 프라이머 설계 : GC는 프라이머의 결합 안정성과 Tm 계산에 필수적.
            - 적절한 GC 함량 : 40 ~ 60 %
        - NGS : GC 함량은 DNA 증폭 및 시퀀싱 효율에 영향을 미침

### 시퀀스 슬라이싱
`Seq`는 문자열과 동일하게 슬라이싱을 통해 특정 인덱스 위치의 서열들을 불러오거나 음수를 이용해 뒤에서부터 서열을 가져올 수 있다.

### Seq 객체를 문자열로 변환
`str()`메서드를 이용해 `Seq`를 문자열로 변환할 수 있다.

### 시퀀스 연결 또는 추가

### 케이스 변경
파이썬 문자열은 대소문자를 바꾸는 데 매우 유용한 `upper`와 `lower`가 있다. `Sep`도 이를 이용할 수 있다.

### 뉴클레오티드 서열 및 (역)보체
`Seq`는 뉴클레오티드 시퀀스의 경우 상보적인 보수와 역보수를 쉽게 구할 수 있다.

##### IUPAC 모호성 코드
| 기호 | 설명                       | 해당 염기           |
|------|----------------------------|---------------------|
| A    | 아데닌                     | A                  |
| T    | 타이민                     | T                  |
| G    | 구아닌                     | G                  |
| C    | 사이토신                   | C                  |
| U    | 유라실 (RNA에서 사용)       | U                  |
| R    | 퓨린 (A 또는 G)            | A, G               |
| Y    | 피리미딘 (C 또는 T)         | C, T               |
| S    | G 또는 C                   | G, C               |
| W    | A 또는 T                   | A, T               |
| K    | G 또는 T                   | G, T               |
| M    | A 또는 C                   | A, C               |
| B    | C, G 또는 T                | C, G, T            |
| D    | A, G 또는 T                | A, G, T            |
| H    | A, C 또는 T                | A, C, T            |
| V    | A, C 또는 G                | A, C, G            |
| N    | 모든 염기 (A, T, G 또는 C) | A, T, G, C         |

### 전사 (Transcription)

**전사**는 유전 정보를 담고 있는 DNA의 특정 부분(유전자)이 **mRNA(메신저 RNA)**로 복사되는 과정입니다. 이는 단백질 합성(번역)으로 이어지는 중심 과정 중 하나로, **중심원리(central dogma)**의 일부입니다.

---

- 전사 과정

    전사는 **진핵생물**과 **원핵생물**에서 약간 다르게 진행되지만, 기본 단계는 유사합니다.

    1. 개시 (Initiation)
        - **RNA 중합효소(RNA polymerase)**가 DNA의 **프로모터(promoter)** 부위에 결합하여 전사를 시작.
        - DNA 이중나선이 풀리며, 주형 가닥(template strand)을 읽기 시작함.

    2. 신장 (Elongation)
        - RNA 중합효소가 DNA의 주형 가닥을 따라 이동하며 **리보뉴클레오타이드(NTP)**를 결합하여 RNA를 합성.
        - 주형 가닥의 염기 서열에 상보적으로 RNA 서열(A-U, G-C)을 생성.

    3. 종결 (Termination)
        - 특정 **종결 신호(terminator)**에 도달하면 RNA 중합효소가 DNA로부터 분리되고, 전사가 종료됨.
        - 생성된 RNA는 **mRNA 전사체(transcript)**라고 함.

---

#### 전사 과정의 세부 특징

1. 주형 가닥과 비주형 가닥
    - **주형 가닥(template strand)**: 전사에 사용되는 DNA 가닥.
    - **비주형 가닥(coding strand)**: 주형 가닥과 상보적이며, 전사된 RNA와 동일한 서열을 가짐(단, T 대신 U).

2. RNA와 DNA의 차이점
    - **RNA**: 리보스 당, U(유라실) 포함.
    - **DNA**: 디옥시리보스 당, T(타이민) 포함.

3. 진핵생물의 전사 후 가공
    - 생성된 RNA는 **전사 후 가공(post-transcriptional modification)** 과정을 거침.
        - **캡핑(capping)**: 5' 말단에 7-메틸구아노신 모자 추가.
        - **폴리A 꼬리(polyadenylation)**: 3' 말단에 다수의 아데닌 염기 추가.
        - **스플라이싱(splicing)**: 인트론(intron)을 제거하고 엑손(exon)을 연결.

---

#### 전사의 생물학적 중요성

1. **단백질 합성의 첫 단계**
   - 전사는 유전 정보를 단백질로 변환하는 번역(translation)의 전 단계.
   
2. **유전자 발현 조절**
   - 프로모터와 조절 서열은 유전자 발현을 조절하며, 세포는 전사 수준에서 유전자 발현을 제어.

3. **유전체 정보의 복사**
   - DNA의 특정 유전자를 mRNA로 복사하여 필요한 단백질을 생성.

---

#### 원핵생물과 진핵생물 전사의 차이점

| 특징               | 원핵생물                                | 진핵생물                                 |
|--------------------|---------------------------------------|----------------------------------------|
| **RNA 중합효소**  | 단일 종류                             | 3가지 종류 (RNA pol I, II, III)        |
| **프로모터**      | -10, -35 서열                        | TATA 상자(TATA box) 등                 |
| **전사 후 가공**  | 없음                                  | 캡핑, 폴리A 꼬리, 스플라이싱 발생       |
| **전사와 번역**   | 동시에 발생                           | 핵에서 전사 후, 세포질로 이동해 번역    |

---

#### 전사 예시

- **DNA 주형 서열**: `3'-TAC GGT ACC-5'`
- **mRNA 서열**: `5'-AUG CCA UGG-3'`

mRNA는 이후 번역 과정에서 리보솜에 의해 **아미노산 서열**로 변환됩니다.
