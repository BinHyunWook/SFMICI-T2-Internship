# Maven 빌드 방법 (Windows)

** 본 어플리케이션은 Java 11에 맞춰져있습니다. **





1. Chocolately 설치
    - 관리자권한으로 CMD 실행
    - `@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command " [System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"`
    
2. OpenJDK 11 설치 (https://docs.microsoft.com/ko-kr/java/openjdk/download) 
   - 17이 아닌 11을 선택하세요.
   - 설치시 JAVAHOME을 PATH에 추가하세요.

3. Maven 설치
    - `choco install maven`
    - `mvn -version` 으로 설치 확인. 

4. 소스코드 수정
    - /src/main/resources/application.properties의 RDS 엔드포인트를 작성한다.

5. 빌드
    - `mvn package -Dmaven.test.skip=true`
    - cmd를 이용하세요. Powershell을 사용시 Maven 에러가 나오는 경우가 있습니다.

6. /target 안의 App S3에 업로드 후 사용
    `aws s3 cp [S3 URI] .`
