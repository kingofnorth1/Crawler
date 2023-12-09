function xsCommon(t, e) {
    try {
      var r,
      n,
      o = t.platform,
      i = e.url,
      a = map_default() (NEED_XSCOMMON_URLS).call(NEED_XSCOMMON_URLS, (function (t) {
        return new RegExp(t)
      }));
      if (!some_default() (a).call(a, (function (t) {
        return t.test(i)
      }))) return e;
      var u = e.headers['X-t'] ||
      '',
      c = e.headers['X-s'] ||
      '',
      s = e.headers['X-Sign'] ||
      '',
      l = getSigCount(u && c || s),
      f = localStorage.getItem(MINI_BROSWER_INFO_KEY),
      p = localStorage.getItem(RC4_SECRET_VERSION_KEY) ||
      RC4_SECRET_VERSION,
      d = {
        s0: getPlatformCode(o),
        s1: '',
        x0: p,
        x1: version,
        x2: o ||
        'PC',
        x3: 'xhs-pc-web',
        x4: '3.19.3',
        x5: js_cookie.Z.get(LOCAL_ID_KEY),
        x6: u,
        x7: c,
        x8: f,
        x9: encrypt_mcr(
          concat_default() (r = concat_default() (n = ''.concat(u)).call(n, c)).call(r, f)
        ),
        x10: l
      };
      e.headers['X-S-Common'] = encrypt_b64Encode(encrypt_encodeUtf8(stringify_default() (d)))
    } catch (h) {
    }
    return e
  }