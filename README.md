# bioinformatics
gene 데이터 크롤링 및 mapping

## Usage
* python Bio 패키지의 문법 및 활용법 정리
* 원하는 종의 accession number를 입력하면 NCBI에서 관련 유전자 관련 데이터를 크롤링해 적절히 정리하여 출력

## Time
* 2020

## Prerequisite
* Bio

## Directories & Files
* practice: biopython 문법 및 활용법 정리
  * 1\. 기본 객체: Seq 및 SeqRecord 객체 소개
    * 1-1. Seq 객체.md
    * 1-2. SeqRecord 객체.md
  * 2\. 고급 기능: 기타 고급 기능 소개
    * 2-1. 파일 읽기.md
    * 2-2. NCBI 데이터 크롤링.md
    * 2-3. BLAST.md
    * 2-4. 계통수.md
    * 2-5. WebLogo.md
    * 2-6. Swiss-Prot.md
    * 2-7. ExPASy.md
    * 2-8. KEGG, KEGG API.md
* source_code: 실전 프로그램 소스코드
  * gene_gathering.py: 유전자 데이터를 txt 파일로 정리해 출력
  * mapping.py: 유전자 관련 데이터를 엑셀 파일로 정리해 출력
