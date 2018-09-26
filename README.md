# django_app-learning_log
这是一个关于网页设计开发的基础练习，参考教材为《python从入门到实践》，这里将记录完整的代码及编写过程中所遇到的一些问
题，以供后续查看并帮助后来的学习者解决遇到的问题。


正文部分
在练习整个项目的时候，大部分时间都是可以完全按照书上写的内容来写的，不会出太多的问题但是当你到了准备部署服务器的时候
可能会遇到一点问题。

问题1：heroku不支持当前python版本时
描述：在编程开始前我使用的是pyhton2.6.7的版本，当开始部署应用到heroku时发现heroku只支持python2.7及python3的版本，
     这个时候我开始下定决心要将自己学习的版本升级到python3以适应未来迟早会到来版本迭代问题。
处理方法：将项目主体从当前文件夹内剪切到其他文件夹
          删除原文件夹及内部所有剩余内容
          在pyhton3环境下新建虚拟环境
          安装与原来版本一致的Django（这点非常重要，血泪的教训，如何查看自己安装的django版本请自行百度这里不再赘述，
          如果你不知道自己以前安装的哪个版本，可以查看原来项目的的setting文件）
          检测能否通过，这里基本上我的已经没有问题了，整个环境已经完全无缝衔接。
          
问题2：Django版本不匹配
描述：转换到python3后默认安装的django版本是2.0以上的版本（而且2.0版本只支持python3了）；django2.0版本相较于1.0的
      版本来说做了大量的改动这是需要重新学习一下框架结构才能了解的所以许多的语法和引用路径都不一样了。
处理方法：卸载2.0版本的django安装你先前使用的版本，具体方法参见问题1.

问题3：项目无法部署到heroku
描述：完全按照书上写的方式，编写好程序后，直接按照指示部署却发现怎么都没法合并上传自己内容老是报错以下内容
       ! Error while running '$ python manage.py collectstatic --noinput'.
        remote: See traceback above for details.
        remote:
        remote: You may need to update application code to resolve this error.
        remote: Or, you can disable collectstatic for this application:
        remote:
        remote: $ heroku config:set DISABLE_COLLECTSTATIC=1
        remote:
        remote: https://devcenter.heroku.com/...
        remote: ! Push rejected, failed to compile Python app.
        remote:
        remote: ! Push failed
        remote: Verifying deploy...
        remote:
        remote: ! Push rejected to protected-crag-1803.
        remote:
        To https://git.heroku.com/protec...
        ! [remote rejected] master -> master (pre-receive hook declined)
        error: failed to push some refs to 'https://git.heroku.com/protec...'
解决方法：参照了论坛https://segmentfault.com/q/1010000010016708内的解决方法，基本的问题有两个，
          第一个是书上的排版问题导致在setting里面heroku的设置写法是错的；
          # 静态资产配置 
          BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
          STATIC_ROOT = 'staticfiles' #这个地方的写法应该是STATIC_ROOT = os.path.join(BASE_DIR, 'static')这样的；
          STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'))
          以上部分的应该是不属于if 结构内的，他们全部要顶格写。
          我把他们全部顶格写之后发现还是一样的报错，这个时候我又回去看那个论坛里面，看到还有一个报错信息就是
          remote: $ heroku config:set DISABLE_COLLECTSTATIC=1
          根据论坛内的方法；在终端里面执行
          heroku config:set DISABLE_COLLECTSTATIC=0
          执行完后再次部署就ok了。
