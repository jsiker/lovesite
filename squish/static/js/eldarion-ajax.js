/**
 * Created by danielsiker on 10/4/14.
 */
/* ====================================================================
 * eldarion-ajax.min.js v0.12.0
 * eldarion-ajax-core v0.10.0
 * eldarion-ajax-handlers v0.1.1
 * ====================================================================
 * Copyright (c) 2013, Eldarion, Inc.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without modification,
 * are permitted provided that the following conditions are met:
 *
 *     * Redistributions of source code must retain the above copyright notice,
 *       this list of conditions and the following disclaimer.
 *
 *     * Redistributions in binary form must reproduce the above copyright notice,
 *       this list of conditions and the following disclaimer in the documentation
 *       and/or other materials provided with the distribution.
 *
 *     * Neither the name of Eldarion, Inc. nor the names of its contributors may
 *       be used to endorse or promote products derived from this software without
 *       specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
 * ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
 * ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 * ==================================================================== */
if(document.all&&!window.setTimeout.isPolyfill){var __nativeST__=window.setTimeout;window.setTimeout=function(e,t){var o=Array.prototype.slice.call(arguments,2);return __nativeST__(e instanceof Function?function(){e.apply(null,o)}:e,t)},window.setTimeout.isPolyfill=!0}if(document.all&&!window.setInterval.isPolyfill){var __nativeSI__=window.setInterval;window.setInterval=function(e,t){var o=Array.prototype.slice.call(arguments,2);return __nativeSI__(e instanceof Function?function(){e.apply(null,o)}:e,t)},window.setInterval.isPolyfill=!0}!function(e){"use strict";var t=function(){};t.prototype._ajax=function(t,o,a,n){t.trigger("eldarion-ajax:begin",[t]);var r=t.triggerHandler("eldarion-ajax:modify-data",n);r&&(n=r),e.ajax({url:o,type:a,dataType:"json",data:n,headers:{"X-Eldarion-Ajax":!0},statusCode:{200:function(e){e||(e={}),t.trigger("eldarion-ajax:success",[t,e])},500:function(){t.trigger("eldarion-ajax:error",[t,500])},400:function(){t.trigger("eldarion-ajax:error",[t,400])},403:function(){t.trigger("eldarion-ajax:error",[t,403])},404:function(){t.trigger("eldarion-ajax:error",[t,404])}},complete:function(o,a){e(document).trigger("eldarion-ajax:complete",[t,o,a])}})},t.prototype.click=function(o){var a=e(this),n=a.attr("href"),r=a.data("method"),c=a.data("data"),l=null,i=null;r||(r="get"),c&&(l={},c.split(",").map(function(t){i=t.split(":"),l[i[0]]=0===i[1].indexOf("#")?e(i[1]).val():i[1]})),o.preventDefault(),t.prototype._ajax(a,n,r,l)},t.prototype.submit=function(o){var a=e(this),n=a.attr("action"),r=a.attr("method"),c=a.serialize();o.preventDefault(),t.prototype._ajax(a,n,r,c)},t.prototype.cancel=function(t){var o=e(this),a=o.attr("data-cancel-closest");t.preventDefault(),o.closest(a).remove()},t.prototype.timeout=function(o,a){var n=e(a),r=n.data("timeout"),c=n.data("url"),l=n.data("method");l||(l="get"),window.setTimeout(t.prototype._ajax,r,n,c,l,null)},t.prototype.interval=function(o,a){var n=e(a),r=n.data("interval"),c=n.data("url"),l=n.data("method");l||(l="get"),window.setInterval(t.prototype._ajax,r,n,c,l,null)},e(function(){e("body").on("click","a.ajax",t.prototype.click),e("body").on("submit","form.ajax",t.prototype.submit),e("body").on("click","a[data-cancel-closest]",t.prototype.cancel),e("[data-timeout]").each(t.prototype.timeout),e("[data-interval]").each(t.prototype.interval)})}(window.jQuery),function(e){"use strict";var t=function(){};t.prototype.redirect=function(e,t,o){return o.location?(window.location.href=o.location,!1):void 0},t.prototype.replace=function(t,o,a){e(o.data("replace")).replaceWith(a.html)},t.prototype.replaceClosest=function(e,t,o){t.closest(t.data("replace-closest")).replaceWith(o.html)},t.prototype.replaceInner=function(t,o,a){e(o.data("replace-inner")).html(a.html)},t.prototype.replaceClosestInner=function(e,t,o){t.closest(t.data("replace-closest-inner")).html(o.html)},t.prototype.append=function(t,o,a){e(o.data("append")).append(a.html)},t.prototype.prepend=function(t,o,a){e(o.data("prepend")).prepend(a.html)},t.prototype.refresh=function(t,o){e.each(e(o.data("refresh")),function(t,o){e.getJSON(e(o).data("refresh-url"),function(t){e(o).replaceWith(t.html)})})},t.prototype.refreshClosest=function(t,o){e.each(e(o.data("refresh-closest")),function(t,a){e.getJSON(e(a).data("refresh-url"),function(t){o.closest(e(a)).replaceWith(t.html)})})},t.prototype.clear=function(t,o){e(o.data("clear")).html("")},t.prototype.remove=function(t,o){e(o.data("remove")).remove()},t.prototype.clearClosest=function(e,t){t.closest(t.data("clear-closest")).html("")},t.prototype.removeClosest=function(e,t){t.closest(t.data("remove-closest")).remove()},t.prototype.fragments=function(t,o,a){a.fragments&&e.each(a.fragments,function(t,o){e(t).replaceWith(o)}),a["inner-fragments"]&&e.each(a["inner-fragments"],function(t,o){e(t).html(o)}),a["append-fragments"]&&e.each(a["append-fragments"],function(t,o){e(t).append(o)}),a["prepend-fragments"]&&e.each(a["prepend-fragments"],function(t,o){e(t).prepend(o)})},e(function(){e(document).on("eldarion-ajax:success",t.prototype.redirect),e(document).on("eldarion-ajax:success",t.prototype.fragments),e(document).on("eldarion-ajax:success","[data-replace]",t.prototype.replace),e(document).on("eldarion-ajax:success","[data-replace-closest]",t.prototype.replaceClosest),e(document).on("eldarion-ajax:success","[data-replace-inner]",t.prototype.replaceInner),e(document).on("eldarion-ajax:success","[data-replace-closest-inner]",t.prototype.replaceClosestInner),e(document).on("eldarion-ajax:success","[data-append]",t.prototype.append),e(document).on("eldarion-ajax:success","[data-prepend]",t.prototype.prepend),e(document).on("eldarion-ajax:success","[data-refresh]",t.prototype.refresh),e(document).on("eldarion-ajax:success","[data-refresh-closest]",t.prototype.refreshClosest),e(document).on("eldarion-ajax:success","[data-clear]",t.prototype.clear),e(document).on("eldarion-ajax:success","[data-remove]",t.prototype.remove),e(document).on("eldarion-ajax:success","[data-clear-closest]",t.prototype.clearClosest),e(document).on("eldarion-ajax:success","[data-remove-closest]",t.prototype.removeClosest)})}(window.jQuery);
