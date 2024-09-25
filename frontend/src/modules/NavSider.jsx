import { Layout } from "antd";
const { Sider } = Layout;

const items = ["概览", "名单", "选项"].map((item, index) => {return {key:index, label: item}})

const NavSider = () => {
    return (
        <>
            <Layout
                style={{
                    padding: '24px 0',
                    background: colorBgContainer,
                    borderRadius: borderRadiusLG,
                }}
            >
                <Sider
                    style={{
                        background: colorBgContainer,
                    }}
                    width={200}
                >
                    <Menu
                        mode="inline"
                        defaultSelectedKeys={['1']}
                        // defaultOpenKeys={['sub1']}
                        style={{
                            height: '100%',
                        }}
                        items={items}
                    />
                </Sider>
            </Layout>
        </>
    )
}

export default NavSider