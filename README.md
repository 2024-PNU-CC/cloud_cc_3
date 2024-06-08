# 프로젝트 명

## 온라인으로 컴파일 가능한 "Web IDE" 서비스
온라인으로 각종 프로그래밍 언어의 소스 코드를 컴파일 할 수 있는, "Web IDE" 서비스입니다. 

# 프로젝트 멤버 이름 및 멤버 별 담당한 파트 소개

- **권내현** 
  * **사용자가 입력한 코드를 RabbitMQ를 통해 전송받은 후 소스코드로 저장합니다.**
  * 저장한 코드를 선택한 언어에 맞게, 웹컴파일러 기능을 통해 실행합니다.
  * 소스코드 실행결과를 전용 데이터베이스 테이블에 저장하여 사용자가 실행 결과를 확인할 수 있도록 합니다.
 
- **정윤서**
   * **프론트엔드(React)와 백엔드(Django)를 연동합니다.**
   * 사용자가 입력한 {소스 코드, 프로그래밍 언어, request_id}를 MySQL 데이터베이스 테이블과 RabbitMQ의 Queue에 추가합니다.
   * 실행 결과가 저장된 데이터베이스 테이블에서 request_id가 일치하는 데이터를 받아와 프론트엔드로 전달합니다.
   * 실행 결과가 데이터베이스 테이블에 저장될 때까지 주기적으로 요청하여 새로고침 없이 실행 결과를 화면에 출력합니다.

- **배명진**
   * **프론트엔드(React)와 백엔드(Django)를 연동합니다.**
   * 사용자가 원하는 프로그래밍 언어, 테마, 코드를 입력하면, 해당 내용을 백엔드(Django) 서버로 전달
   * 적절한 요청에 대한 응답을 받을 때까지 백엔드에게 요청을 반복적(2초 간격)으로 보냅니다. 해당 반복은 적절한 요청 응답을 받거나, 사용자가 '초기화'버튼을 누르면 중단됩니다.
   * 백엔드로부터 받은 응답을 '컴파일 결과' 화면에 출력합니다.

- **최범주**
   * **코드를 seccomp를 통해 안전하게 실행하고 인프라를 구성합니다.**
   * fork bomb 등의 악의적인 코드를 안전하게 실패하게 합니다.
   * 샌드박스에서 실행될 언어에 맞는 코드 환경을 구성합니다.
   * on premise와 azure를 하이브리드로 구성합니다.
 

# 프로젝트 소개
> 사용자가 로컬 환경에 별도의 IDE(통합 개발 환경)를 설치하지 않아도 웹 브라우저를 통해 코드를 작성하고, 작성한 코드의 컴파일 및 실행 결과를 확인할 수 있는 웹 기반 통합 개발 환경(Web IDE) 및 컴파일러입니다.

- 이 프로젝트는 다양한 프로그래밍 언어(C++, Python, Rust, Go)를 지원하며, 인터넷에 연결되어 있는 사용자가 **언제 어디서나 편리하게** 코딩할 수 있도록 지원합니다. 
- 서비스의 **안정성 및 보안을 위해 기능이 사용자별로 컨테이너화되어 제공**됩니다. 따라서 코드의 실행 결과는 작성자만 확인할 수 있습니다. 

# 프로젝트 필요성 소개

## 높은 접근성과 편의성
&nbsp;현대 개발자는 여러 언어를 동시에 다루는 경우가 많습니다. 각 언어마다 필요한 컴파일러 및 IDE가 다르기 때문에 개발자의 로컬 저장소에는 많은 컴파일러 및 IDE가 설치되어 있어야 합니다. 만약, 초기 환경 구축, 기기 변경 등이 발생할 경우, 개발 환경을 구축하는 데에 시간적 비용이 많이 소요됩니다. 

&nbsp;만약 해당 서비스를 이용한다면, **개발자가 초기 구축 과정이 필요하지 않아 접근성이 높은 개발 환경을 제공받게 되어 보다 편리하게 개발에 몰두할 수 있습니다.**

&nbsp;강의실에서 개발환경이 미리 세팅된 PC로 프로그래밍 실습이 이루어지는 경우도 있지만, 대부분의 경우에는 따로 노트북을 들고 다녀야 하는 경우가 많습니다.

&nbsp; 태블릿을 사용하여 개발 실습을 수행하는 경우, PC보다 개발환경의 접근성이 떨어지기 때문에 프로그래밍 과목을 들을 때 어려움을 겪는 경우가 많습니다. 따라서 웹 기반 컴파일 서비스는 **모바일 및 타블렛**을 이용해도 코드 작성 및 컴파일 결과 확인이 가능하도록 함으로써 사용자에게 편리함을 제공하였습니다.

## 통일된 개발 환경 제공
&nbsp;최근 교육과정에서 프로그래밍을 다루는 비중이 점점 커짐에 따라 IT 비전공자들이 프로그래밍 관련 과목을 수강하는 사례가 증가하고 있습니다. 그러나 학교 등 각종 교육 환경에서 프로그래밍 언어를 교육할 때, **복잡한 설치 과정, IDE 또는 컴파일러 버전의 차이 등으로 인해 수업 진행에 차질을 겪는 경우가 많습니다.** 

&nbsp;해당 서비스를 사용하면 **교육자와 학습자가 모두 동일한 환경에서 프로그래밍 학습을 하는 것이 보장**됩니다. 그러므로 프로그래밍 언어의 버전에 따라 구현 방식의 차이로 인해 학습자가 겪을 혼란을 방지할 수 있습니다.

# 관련 기술 / 논문 / 특허 조사 내용 소개
## [구름 IDE](https://help.goorm.io/ko/goormide/getting-started/what-is-goormide)
&nbsp;클라우드 통합 개발 환경(CDE)으로, 소프트웨어 개발에 필요한 여러 프로그래밍
언어(Python, JavaScript, JAVA, C/C++)를 지원합니다. 웹 브라우저 상에서 코드 편집, 컴파일, 실행 등의 작업을 할 수 있습니다. 또한, 실시간 협업 기능을 제공하여 동일한 코드를 여러 명의 개발자가 동시에 편집할 수 있습니다. 구름은 컨테이너를 사용하면 사용한 만큼 크레딧이 차감되는 ‘pay-as-you-go’ 방식을 채용하고 있는 부분 유료화 서비스입니다.

&nbsp;구름 IDE에서는 클라우드 기술의 특징을 확인할 수 있습니다. '컨테이너'에서 클라우드의 기본적인 성격을 확인할 수 있으며, 컨테이너는 독립적인 개발 환경 및 클라우드 환경에서 실행되는 가상 머신을 의미합니다. '팀'은  조직의 구성원을 묶는 단위를 말하며, 구름 IDE에서 클라우드 구성원을 정의하는 방식입니다. 이 '팀' 기능을 이용해 각 팀원에게 특정 권한을 설정할 수 있습니다.

&nbsp;안정성 및 보안을 위해 WebIDE의 기능을 사용자별로 컨테이너화하여 제공하는 기능은 구름IDE의 컨테이너 시스템에서 착안한 기능입니다.

## [Codingground](https://www.tutorialspoint.com/codingground.htm)
&nbsp;웹 컴파일러로서, Python, JAVA, C++ 등 다양한 언어를 지원하는 시스템입니다. 웹 브라우저 상에서 바로 코드 편집 및 컴파일, 실행이 가능합니다. 회원가입 및 로그인을 필요로 하지 않으나, 이미 작성한 코드를 웹상으로 불러올 수 없으며, 사이트를 새로고침할 시 작성 중이던 코드가 모두 초기화된다는 단점이 있습니다.

# 프로젝트 개발 결과물 소개 (+ 다이어그램)

## 시스템 전체 구상도
![Diagram_0605](https://github.com/2024-PNU-CC/judger/assets/108617949/6602d3f5-3ea3-4caf-bb0c-45657eedad2e)

## 작동 매커니즘

* 인프라
  - 메모리 부족 등 성능 문제가 자주 발생해 하이브리드로 구성했습니다.
  - 프론트엔드로 부터 요청이 발생하면, cloudflare가 수신해 온프레미스 환경의 nginx로 연결됩니다.
  - nginx는 azure의 인스턴스에 있는 백엔드로 요청을 보냅니다.
  - 백엔드에서 온프레미스 환경의 Rabbit MQ, MySQL와 통신합니다.
* 프론트엔드
  - 사용자로부터 프로그래밍 언어, 테마, 소스 코드를 입력받습니다.
  - 사용자가 '컴파일' 버튼을 누르면, 고유 id를 생성합니다. 이후 백엔드에 {request_id, 작성 언어, 소스코드} 데이터를 전송하여 컴파일을 요청합니다.
  - 이후, 백엔드로부터 적절한 응답이 왔는지 2초 간격으로 반복적으로 확인합니다. 만약 적절한 응답이 왔다면 '컴파일 결과' 화면에 컴파일 결과를 출력합니다. 만약 적절한 응답이 없다면 계속해서 확인합니다.
  - 이 때, 사용자가 '초기화' 버튼을 누르게 되면, 프로그래밍 언어, 테마, 소스 코드는 기본값으로 설정되게 되고, 백엔드에게 반복적으로 보내던 요청도 중단하게 됩니다.
* 백엔드
  - 프론트엔드에서 받아온 {request_id, 작성 언어, 소스코드} 데이터를 데이터베이스의 'submissions_submission' 테이블에 저장합니다. 또한 동일한 데이터를 RabbitMQ에 json 형태로 입력합니다.
  - RabbitMQ에 {request_id, 작성 언어, 소스코드} 데이터가 입력됨을 감지하면, 실행 중이던 go 프로그램에서 해당 데이터를 읽어옵니다. 이렇게 읽어 온 JSON 데이터를 저장한 후, 소스코드를 파일로 저장합니다.
  - 이후, yaml 파일을 이용해 저장된 소스코드에 오류가 없는지 확인한 후, 언어 형식에 맞게 소스 코드를 실행합니다. 소스코드의 실행 결과는 go 프로그램이 실행되고 있는 로컬에 output.txt의 형태로 저장됩니다. 만약 컴파일, 또는 런타임 도중에 오류가 발생했을 경우 compile_error.txt 파일에 상세한 오류가 저장됩니다.
  - 코드의 수행 결과를 'cc_schema'라는 데이터베이스의 'submissions_coderesult' 테이블에 저장합니다. 코드가 정상적으로 실행되었을 경우에는 output.txt의 내용을, 코드 실행 중 오류가 발생하여 정상적으로 완료되지 않았을 경우에는 compile_error.txt의 내용을 저장합니다. 사용자가 보낸 코드는 request_id를 통해 구별되기 때문에, 수행 결과를 데이터베이스에 저장할 때에도 request_id를 같이 저장해줍니다.
* DB & Web
  - 프론트에서 작성한 코드를 컴파일 버튼을 눌러 전송한 후, DB에서 'submissions_coderesult' 테이블에서 자신의 request_id와 일치하는 결과가 있는지 확인합니다. 
  - 테이블은 2초에 한 번씩 확인하며, 만약 테이블에서 자신의 request_id와 일치하는 코드 실행 결과가 감지했을 경우 테이블에서 코드 실행 결과를 읽어온 후 웹페이지의 컴파일 결과 창에 출력합니다. 
  - 만약 테이블에서 제한시간 내에 자신의 request_id와 일치하는 코드 실행 결과를 감지하지 못하면 'Error fetching result'를 웹페이지의 컴파일 결과 창에 출력합니다.
  - 코드 작성 창의 테마를 Light mode / Dark mode 중 하나로 선택할 수 있습니다.

## 시스템 사용 조건
&nbsp;사용자는 시스템을 사용하기 위해 인터넷에 연결되어 있어야 하며, 사용자가 원하는 프로그래밍 언어를 선택한 상태로 소스코드를 작성 및 컴파일해야 합니다. 그 외의 조건 및 자격은 필요하지 않습니다. 

&nbsp;아래의 세 조건이 충족되어 있으면 시스템은 정상적으로 작동합니다.
- 백엔드 서버가 실행되고 있는 상태여야 합니다.
- go.main 소스코드가 실행되고 있는 상태여야 합니다.

# 개발 결과물을 사용하는 방법 소개 (설치 방법, 동작 방법 등)

## 설치 방식
&nbsp;기능을 담당하는 원격 서버가 동작하고 있기 때문에 웹사이트에 접속하는 것을 제외한 **별도의 설치 과정은 필요하지 않습니다.**
## 동작 방법
1. https://fc.fiene.dev/ 에 접속합니다.
2. 작성하고자 하는 언어 형식을 드롭-다운 방식을 통해 선택한 후, 언어 형식에 맞게 코드를 작성합니다. 
3. 코드를 작성한 후에는 컴파일 버튼을 눌러 원격 서버로 코드를 전송합니다. 버튼을 누르면 코드가 자동으로 전송됩니다.
4. '컴파일 결과' 화면에서, 컴파일 결과를 확인합니다.
    * 컴파일 및 실행 후 에러가 발생하지 않았다면, 정상적으로 실행 결과가 창에 출력됩니다.
    * 컴파일 및 실행 후 에러가 발생했다면, 발생한 에러가 '컴파일 결과' 화면에 출력됩니다.

# 개발 결과물의 활용방안 소개
&nbsp;개발자가 흔히 사용하는 Visual Studio 등의 통합 IDE는 높은 성능과 다양한 플러그인 등을 지원하여 사용자가 동시에 많은 개발 언어를 다루는 데에 도움을 줄 수 있습니다.

&nbsp;하지만 Visual Studio는 설치된 기능에 따라 최소 850MB, 최대 210GB의 공간이 필요하며, 일반적인 설치에는 20~50GB의 스토리지 공간이 필요합니다. 그렇기에 스토리지 공간이 부족하면 Visual Studio를 사용했을 때 오히려 불편한 경우가 발생할 수 있습니다.

&nbsp;이러한 경우에 저희가 개발한 서비스를 사용한다면, **다양한 언어의 공부 및 개발에서 사용자에게 높은 접근성과 편의성을 제공받을 수 있습니다.** PC가 없는 상황에서 모바일 기기 및 태블릿으로 간단한 프로그래밍을 할 수 있으며, 각종 프로그래밍 수업에서 교육자 간의 통일된 환경을 보장할 수 있기 때문에 'Web IDE' 서비스는 높은 가치를 지닐 것입니다.
