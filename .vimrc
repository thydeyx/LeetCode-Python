set rtp+=~/.vim/bundle/Vundle.vim/
call vundle#rc()
Bundle 'gmarik/vundle'

" 设置当文件被改动时自动载入
set autoread
"自动保存
set autowrite
set ruler                   " 打开状态栏标尺*/
set cursorline              " 突出显示当前行*/*/
set magic                   " 设置魔术*/
"set statusline=\ %<%F[%1*%M%*%n%R%H]%=\ %y\ %0(%{&fileformat}\ %{&encoding}\ %c:%l/%L%)\
" 设置在状态行显示的信息
"set foldcolumn=0
"set foldmethod=indent 
"set foldlevel=3 
"set foldenable              " 开始折叠
" 不要使用vi的键盘模式，而是vim自己的
set nocompatible
" 语法高亮
"set syntax=on
syntax on
" 去掉输入错误的提示声音
set noeb
" 在处理未保存或只读文件的时候，弹出确认
set confirm
" 自动缩进
set autoindent
set cindent
" Tab键的宽度
set tabstop=4
" 统一缩进为4
set softtabstop=4
set shiftwidth=4
" 不要用空格代替制表符
set noexpandtab
" 在行和段开始处使用制表符
set smarttab
" 显示行号
set number
" 历史记录数
set history=1000
"禁止生成临时文件
set nobackup
set noswapfile
"搜索忽略大小写
set ignorecase
"搜索逐字符高亮
set hlsearch
set incsearch
"行内替换
"set gdefault
"编码设置
set enc=utf-8


map <F5> <C-w>h "左
map <F6> <C-w>l "右
map <F8> <C-w>j "下
map <F7> <C-w>k "上
map <F9> :qa<CR> "退出所有页面 
map <F10> \c<space> "注释
map <F2> :w<CR> 

Bundle 'majutsushi/tagbar'
"nmap <Leader>tb :TagbarToggle<CR>        "快捷键设置
let g:tagbar_ctags_bin='ctags'            "ctags程序的路径
let g:tagbar_width=30                    "窗口宽度的设置
map <F3> :Tagbar<CR>
autocmd BufReadPost *.py,*.cpp,*.c,*.h,*.hpp,*.cc,*.cxx call tagbar#autoopen()     "如果是c语言的程序的话，tagbar自动开启

let g:python_author = 'TangHanYi'
let g:python_email  = 'thydeyx@163.com'

function HeaderPython()
	normal 1G
	call setline(".", "# -*- coding:utf-8 -*-")
	normal o
	call setline(".", "#")
	normal o
	call setline(".", "#        Author : ".g:python_author)
	normal o
	call setline(".", "#        E-mail : ".g:python_email)
	normal o
	call setline(".", "#   Create Date : ".strftime("%Y-%m-%d %X" ))
	normal o
	call setline(".", "# Last modified : ".strftime("%Y-%m-%d %X" ))
	normal o
	call setline(".", "#     File Name : ".expand("%"))
	normal o
	call setline(".", "#          Desc :")
	normal o
	normal o
	normal o
	call setline(".", "if __name__ == \"__main__\":")
	normal o
	call setline(".", "\ts = Solution()")
endf
autocmd bufnewfile *.py call HeaderPython()

autocmd BufWrite,BufWritePre,FileWritePre  *.py    ks|call LastModified()|'s    
func LastModified()  
	if line("$") > 20  
		let l = 20  
	else   
		let l = line("$")  
	endif  
	exe "1,".l."g/# Last modified : /s/# Last modified : .*/# Last modified :". strftime(" %Y-%m-%d %X" ) . "/e"  
endfunc  

function HeaderCPP()
	normal 1G
	call setline(".", "//      Author : ".g:python_author)
	normal o
	call setline(".", "//      E-mail : ".g:python_email)
	normal o
	call setline(".", "// Create Date : ".strftime("%y-%m-%d %H:%M:%S"))
	normal o
	call setline(".", "//   File Name : ".expand("%"))
	normal o
	call setline(".", "//        Desc :")
	normal o
	normal o
	normal o
	call setline(".", "#include<iostream>")
	normal o
	call setline(".", "using namespace std;")
	normal o
	normal o
	call setline(".", "int main()")
	normal o
	call setline(".", "{")
	normal o
	call setline(".", "\treturn 0;")
	normal o
	call setline(".", "}")
endf
autocmd bufnewfile *.cpp call HeaderCPP()

Bundle 'scrooloose/nerdtree'
let NERDTreeWinPos='left'
let NERDTreeWinSize=30
let NERDChristmasTree=0
let NERDTreeChDirMode=2
let NERDTreeIgnore=['\~$', '\.pyc$', '\.swp$']
let NERDTreeShowBookmarks=1
"map <F2> :NERDTreeToggle<CR>
autocmd vimenter * NERDTree

Bundle 'fholgado/minibufexpl.vim'
let g:miniBufExplMapWindowNavVim = 1   
let g:miniBufExplMapWindowNavArrows = 1   
let g:miniBufExplMapCTabSwitchBufs = 1   
let g:miniBufExplModSelTarget = 1  
let g:miniBufExplMoreThanOne=0
map <F11> :MBEbp<CR>
map <F12> :MBEbn<CR>

"Bundle 'bling/vim-airline'
"set laststatus=2

Plugin 'Valloric/YouCompleteMe'

let g:ycm_global_ycm_extra_conf='~/.vim/bundle/YouCompleteMe/third_party/ycmd/cpp/ycm/.ycm_extra_conf.py'
let g:ycm_error_symbol = '>>'
let g:ycm_warning_symbol = '>*'
set completeopt=longest,menu	"让Vim的补全菜单行为与一般IDE一致(参考VimTip1228)
autocmd InsertLeave * if pumvisible() == 0|pclose|endif	"离开插入模式后自动关闭预览窗口
"youcompleteme  默认tab  s-tab 和自动补全冲突
"let g:ycm_key_list_select_completion=['<c-n>']
let g:ycm_key_list_select_completion = ['<Down>']
"let g:ycm_key_list_previous_completion=['<c-p>']
let g:ycm_key_list_previous_completion = ['<Up>']
let g:ycm_confirm_extra_conf=0 "关闭加载.ycm_extra_conf.py提示
"在注释输入中也能补全
let g:ycm_complete_in_comments = 1
"在字符串输入中也能补全
let g:ycm_complete_in_strings = 1
"注释和字符串中的文字也会被收入补全
let g:ycm_collect_identifiers_from_comments_and_strings = 0
let g:ycm_seed_identifiers_with_syntax=1	" 语法关键字补全
"let g:loaded_youcompleteme=1

syntax enable
set background=dark
colorscheme solarized
let g:solarized_termcolors=256

"Bundle "scrooloose/syntastic"
" configure syntastic syntax checking to check on open as well as save
"set statusline+=%#warningmsg#
"set statusline+=%{SyntasticStatuslineFlag()}
"set statusline+=%*
"let g:syntastic_always_populate_loc_list = 1
"let g:syntastic_auto_loc_list = 1
"let g:syntastic_check_on_open = 1
"let g:syntastic_check_on_wq = 0

Bundle "scrooloose/nerdcommenter"
let g:NERDAltDelims_python = 1
let g:NERDCompactSexyComs = 1

"filetype plugin on
"let g:pydiction_location = '/home/ubuntu/.vim/bundle/pydiction/complete-dict'
"let g:pydiction_menu_height = 20
