/*
 中国人保 App 去广告 — Egern 原生脚本
 由 Surge/Loon/QX 脚本移植（原作者 Sliverkiss，2024-02-18），
 脚本逻辑不变，运行时 API 换为 Egern ctx。
 来源:
 - fmz200/wool_scripts Scripts/picc/picc_ads.js
 - Moli-X/Tool Loon/Plugin/Kelee/Script/PICC_Insurance_remove_ads.js
*/
export default async function (ctx) {
  const body = await ctx.response.json();
  const url = ctx.request.url;

  const actions = {
    homeInit: () => {
      body.data.startupPage = {};
      body.data.templates = body.data.templates.filter(
        (e) =>
          !e.name.match(
            /主轮播图|保险推荐|专享|腰封轮播图|浮标配置|二楼营销位|首页主题/,
          ),
      );
    },
    myPageConfigList: () => {
      body.data.YFList = [];
    },
  };

  const actionKey = Object.keys(actions).find((key) => url.includes(key));
  actions[actionKey]?.();

  return { body: JSON.stringify(body) };
}
