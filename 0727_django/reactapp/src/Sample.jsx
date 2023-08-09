function Sample(props) {
  //   return <div>함수형 컴포넌트</div>;

  // 자바스크립트의 구조 분해 할당
  // = 오른쪽에 객체를 설정하고
  // 왼쪽에 {} 안에 변수를 설정하면, 변수 이름과 동일한 객체의 속성이 분해되서 대입됨.
  const { album, children } = props;

  return (
    <>
      <div>
        두 번째 앨범은 {album} 태그안의 내용은 {children}
        배드민턴치러 간다. 이히힣   
      </div>
    </>
  );
}

export default Sample;
