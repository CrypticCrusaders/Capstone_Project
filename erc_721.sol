// SPDX-License-Identifier: MIT

pragma solidity ^0.8.11;

interface IERC721 {

    
    function ownerOf(uint256 tokenId) external view returns (address owner);

    function transferFrom(
        address from,
        address to,
        uint256 tokenId
    ) external;


} 