import { Layout, theme, Menu } from "antd";
const { Sider } = Layout;

const items = ["概览", "名单", "选项"].map((item, index) => { return { key: index, label: item } })

const NavSider = () => {
  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken();
  return (
    <>

      <Sider
        style={{
          background: colorBgContainer,
        }}
        width={200}
      >
        <Menu
          mode="inline"
          defaultSelectedKeys={['1']}
          defaultOpenKeys={['1']}
          style={{
            height: '100%',
          }}
          items={items}
        />
      </Sider>
    </>
  )
}

export default NavSider