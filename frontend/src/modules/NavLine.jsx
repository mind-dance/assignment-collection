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
        {items.map((item) => (
          <Breadcrumb.Item key={item.key}>{item.label}</Breadcrumb.Item>
        ))}
      </Breadcrumb>
    </>
  )
}

export default NavLine