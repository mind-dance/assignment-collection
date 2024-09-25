import { Breadcrumb } from "antd";

// const items = props.gps.map((item) => ({}))


const NavLine = (props) => {
  const items = props.gps.map((item, index) => ({ key: index, label: item }));
  return (
    <>
      <Breadcrumb
        style={{
          margin: '16px 0',
        }}
      >

        <Breadcrumb items={[
          { label: 'Home' },
          { label: 'Page 1' }
        ]} />
      </Breadcrumb>
    </>
  )
}

export default NavLine