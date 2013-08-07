/* YUI 3.8.1 (build 5795) Copyright 2013 Yahoo! Inc. http://yuilibrary.com/license/ */
YUI.add("event-custom-complex",function(e,t){var n,r,i,s={},o=e.CustomEvent.prototype,u=e.EventTarget.prototype,a=function(e,t){var n;for(n in t)r.hasOwnProperty(n)||(e[n]=t[n])};e.EventFacade=function(e,t){e=e||s,this._event=e,this.details=e.details,this.type=e.type,this._type=e.type,this.target=e.target,this.currentTarget=t,this.relatedTarget=e.relatedTarget},e.mix(e.EventFacade.prototype,{stopPropagation:function(){this._event.stopPropagation(),this.stopped=1},stopImmediatePropagation:function(){this._event.stopImmediatePropagation(),this.stopped=2},preventDefault:function(){this._event.preventDefault(),this.prevented=1},halt:function(e){this._event.halt(e),this.prevented=1,this.stopped=e?2:1}}),o.fireComplex=function(t){var n,r,i,s,o,u,a,f,l,c=this,h=c.host||c,p,d;if(c.stack&&c.queuable&&c.type!=c.stack.next.type)return c.stack.queue.push([c,t]),!0;n=c.stack||{id:c.id,next:c,silent:c.silent,stopped:0,prevented:0,bubbling:null,type:c.type,afterQueue:new e.Queue,defaultTargetOnly:c.defaultTargetOnly,queue:[]},f=c.getSubs(),c.stopped=c.type!==n.type?0:n.stopped,c.prevented=c.type!==n.type?0:n.prevented,c.target=c.target||h,c.stoppedFn&&(a=new e.EventTarget({fireOnce:!0,context:h}),c.events=a,a.on("stopped",c.stoppedFn)),c.currentTarget=h,c.details=t.slice(),c._facade=null,r=c._getFacade(t),e.Lang.isObject(t[0])?t[0]=r:t.unshift(r),f[0]&&c._procSubs(f[0],t,r),c.bubbles&&h.bubble&&!c.stopped&&(d=n.bubbling,n.bubbling=c.type,n.type!=c.type&&(n.stopped=0,n.prevented=0),u=h.bubble(c,t,null,n),c.stopped=Math.max(c.stopped,n.stopped),c.prevented=Math.max(c.prevented,n.prevented),n.bubbling=d),c.prevented?c.preventedFn&&c.preventedFn.apply(h,t):c.defaultFn&&(!c.defaultTargetOnly&&!n.defaultTargetOnly||h===r.target)&&c.defaultFn.apply(h,t),c._broadcast(t);if(f[1]&&!c.prevented&&c.stopped<2)if(n.id===c.id||c.type!=h._yuievt.bubbling){c._procSubs(f[1],t,r);while(p=n.afterQueue.last())p()}else l=f[1],n.execDefaultCnt&&(l=e.merge(l),e.each(l,function(e){e.postponed=!0})),n.afterQueue.add(function(){c._procSubs(l,t,r)});c.target=null;if(n.id===c.id){s=n.queue;while(s.length)i=s.pop(),o=i[0],n.next=o,o.fire.apply(o,i[1]);c.stack=null}return u=!c.stopped,c.type!=h._yuievt.bubbling&&(n.stopped=0,n.prevented=0,c.stopped=0,c.prevented=0),c._facade=null,u},o._getFacade=function(){var t=this._facade,n,r=this.details;return t||(t=new e.EventFacade(this,this.currentTarget)),n=r&&r[0],e.Lang.isObject(n,!0)&&(a(t,n),t.type=n.type||t.type),t.details=this.details,t.target=this.originalTarget||this.target,t.currentTarget=this.currentTarget,t.stopped=0,t.prevented=0,this._facade=t,this._facade},o.stopPropagation=function(){this.stopped=1,this.stack&&(this.stack.stopped=1),this.events&&this.events.fire("stopped",this)},o.stopImmediatePropagation=function(){this.stopped=2,this.stack&&(this.stack.stopped=2),this.events&&this.events.fire("stopped",this)},o.preventDefault=function(){this.preventable&&(this.prevented=1,this.stack&&(this.stack.prevented=1))},o.halt=function(e){e?this.stopImmediatePropagation():this.stopPropagation(),this.preventDefault()},u.addTarget=function(t){this._yuievt.targets[e.stamp(t)]=t,this._yuievt.hasTargets=!0},u.getTargets=function(){return e.Object.values(this._yuievt.targets)},u.removeTarget=function(t){delete this._yuievt.targets[e.stamp(t)]},u.bubble=function(e,t,n,r){var i=this._yuievt.targets,s=!0,o,u=e&&e.type,a,f,l,c,h=n||e&&e.target||this,p;if(!e||!e.stopped&&i)for(f in i)if(i.hasOwnProperty(f)){o=i[f],a=o.getEvent(u,!0),c=o.getSibling(u,a),c&&!a&&(a=o.publish(u)),p=o._yuievt.bubbling,o._yuievt.bubbling=u;if(!a)o._yuievt.hasTargets&&o.bubble(e,t,h,r);else{a.sibling=c,a.target=h,a.originalTarget=h,a.currentTarget=o,l=a.broadcast,a.broadcast=!1,a.emitFacade=!0,a.stack=r,s=s&&a.fire.apply(a,t||e.details||[]),a.broadcast=l,a.originalTarget=null;if(a.stopped)break}o._yuievt.bubbling=p}return s},n=new e.EventFacade,r={};for(i in n)r[i]=!0},"3.8.1",{requires:["event-custom-base"]});
